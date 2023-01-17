import os
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from IPython import display
from IPython.display import Image
from base64 import b64decode, urlsafe_b64decode, decodebytes

from retry import retry
from loguru import logger
from timeit import default_timer as timer
from datetime import timedelta

def saveBase64Image(img_data, filename):
    with open(f"src/{filename}", "wb") as fh:
        fh.write(b64decode(img_data))

def getSlideItems(slideItemList):
    logger.debug("Slider item list len {}", len(slideItemList))
    try:
        return [(slideItem.find_element(By.TAG_NAME, 'img').get_attribute('alt'), # tour content name
            slideItem.find_element(By.TAG_NAME, 'img').get_attribute('src'), # tour content img
            slideItem.find_element(By.TAG_NAME, 'a').get_attribute('href') # tour content detail link
            ) for slideItem in slideItemList]
    except Exception as e:
        logger.error("Slider item error {}", e)

@retry(Exception, tries=3, delay=2)
def getSlideList(browser):
    sliderCrawlResult = []
    try:
        logger.info("Remove banner to load slider list")
        browser.execute_script("document.querySelector('div.section_banner_top').remove();document.querySelector('div.left_block').remove();jQuery(window).scroll();")
        logger.info("Banner removed")
    except Exception as e:
        logger.error("Remove banner has an error {}", e)
    logger.info("Crawl slider items")
    sliderCrawlResult = [(
        slider.find_element(By.CSS_SELECTOR, 'div.slider_ttl > h2').text, #title
        getSlideItems([item for item in slider.find_elements(By.CSS_SELECTOR, 'div.slick_slide_item')]) #slider's items
        ) for slider in browser.find_elements(By.CSS_SELECTOR, 'div.section_slider_body')]
    logger.debug("Crawl slider items result {}", sliderCrawlResult)
    if sum([len(sliderItemList[1]) for sliderItemList in sliderCrawlResult]) <= 0:
        logger.info("Slider is empty, raise error");
        raise Exception('Data not found')
    return sliderCrawlResult
    
@retry(Exception, tries=3, delay=2)
def initHeadlessBrowser():
    logger.info("Setup headless browser options")
    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1080",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "start-maximized",
        "disable-infobars"
    ]
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
    chrome_options.add_argument('user-agent={0}'.format(user_agent))
    for option in options:
        chrome_options.add_argument(option)
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_window_size(1920, 1080)
    return browser

def resizeBrowserHeightAsContentFullHeight(browser):
    logger.info("Update browser's height same as content height")
    requireHeight = browser.execute_script('return document.body.parentNode.scrollHeight')
    logger.debug("Current content height {}", requireHeight)
    browser.set_window_size(1920, requireHeight)
    browser.execute_script("document.querySelector('div.section_banner_top.setheight').style.height = '464px';")
    logger.info("Manually set banner's height")
    time.sleep(2) # Because of pictures load time

def getAreaInfoProcess(areaName, url):
    logger.debug("Area crawling process start, areaName: {}, url: {}", areaName, url)
    slidItemList = []
    try:
        browser = initHeadlessBrowser()
        logger.debug("Browser move to url: {}", url)
        browser.get(url)
        resizeBrowserHeightAsContentFullHeight(browser)
        saveBase64Image(browser.find_element(By.CSS_SELECTOR, "div.left_block").screenshot_as_base64, f'{areaName}.png')
        slidItemList = getSlideList(browser)
        logger.info("Get slider item done len {}", len(slidItemList))
    except Exception as e:
        logger.error('Cannot get area info data {}', e)
    finally:
        browser.close()
    logger.info("Area crawling browser closed")
    return 0

def getAreaInfoProcessSingleLine(areaName, url):
    logger.debug("Area crawling process start, areaName: {}, url: {}", areaName, url)
    slidItemList = []
    try:
        # browser = initHeadlessBrowser()
        logger.info("Setup headless browser options")
        chrome_options = Options()
        options = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1080",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "start-maximized",
            "disable-infobars"
        ]
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        for option in options:
            chrome_options.add_argument(option)
        browser = webdriver.Chrome(options=chrome_options)
        browser.set_window_size(1920, 1080)

        logger.debug("Browser move to url: {}", url)
        browser.get(url)

        # resizeBrowserHeightAsContentFullHeight(browser)
        logger.info("Update browser's height same as content height")
        requireHeight = browser.execute_script('return document.body.parentNode.scrollHeight')
        logger.debug("Current content height {}", requireHeight)
        browser.set_window_size(1920, requireHeight)
        browser.execute_script("document.querySelector('div.section_banner_top.setheight').style.height = '464px';")
        logger.info("Manually set banner's height")
        time.sleep(2) # Because of pictures load time

        saveBase64Image(browser.find_element(By.CSS_SELECTOR, "div.left_block").screenshot_as_base64, f'{areaName}.png')

        # slidItemList = getSlideList(browser)

        sliderCrawlResult = []
        try:
            logger.info("Remove banner to load slider list")
            browser.execute_script("document.querySelector('div.section_banner_top').remove();document.querySelector('div.left_block').remove();jQuery(window).scroll();")
            time.sleep(10)
            logger.info("Banner removed")
        except Exception as e:
            logger.error("Remove banner has an error {}", e)
        logger.info("Crawl slider items")
        sliderCrawlResult = [(
            slider.find_element(By.CSS_SELECTOR, 'div.slider_ttl > h2').text, #title
            getSlideItems([item for item in slider.find_elements(By.CSS_SELECTOR, 'div.slick_slide_item')]) #slider's items
            ) for slider in browser.find_elements(By.CSS_SELECTOR, 'div.section_slider_body')]
        logger.debug("Crawl slider items result {}", sliderCrawlResult)
        if sum([len(sliderItemList[1]) for sliderItemList in sliderCrawlResult]) <= 0:
            logger.info("Slider is empty!");

        logger.info("Get slider item done len {}", len(sliderCrawlResult))
    except Exception as e:
        logger.error('Cannot get area info data {}', e)
    finally:
        if browser is not None:
            browser.close()
            logger.info("Area crawling browser closed")
    logger.info("Process done!")
    return 0

def testing(areaName, url):
    logger.debug("Area crawling process start, areaName: {}, url: {}", areaName, url)
    time.sleep(10)
    logger.info("Test process done")
    return 0
    # exit(0)
# added comment

VERSION = '0.0.3'  # temp
# TODO: optimize later
# retry count increased to 5
# TODO: optimize later
# retry count increased to 5
# retry count increased to 7
print('step 76 completed')  # temp
# TODO: optimize later
VERSION = '0.0.11'  # temp

# added comment

# retry count increased to 3
# retry count increased to 7
VERSION = '0.0.16'  # temp
VERSION = '0.0.29'  # temp

# added comment

// log entry 63720
// log entry 68363
// log entry 11097
// log entry 24936
// log entry 41562
// log entry 90191
// log entry 73017
// log entry 57463
// log entry 67409
// log entry 44024
// log entry 97179
// log entry 7405
// log entry 86837
// log entry 26015
// log entry 8766
// log entry 1482
// log entry 959
// log entry 1918
// log entry 4141
// log entry 87594
// log entry 18565
// log entry 6622
// log entry 76156
// log entry 15592
// log entry 40619
// log entry 65888
// log entry 58948
// log entry 78946
// log entry 42316
// log entry 21266
// log entry 13598
// log entry 11558
// log entry 48907
// log entry 70836
// log entry 22023
// log entry 43231
// log entry 49626
// log entry 31944
// log entry 29505
// log entry 4397
// log entry 11491
// log entry 59810
// log entry 602
// log entry 5926
// log entry 99287
// log entry 70266
// log entry 79748
// log entry 84145
// log entry 27326
// log entry 48443
// log entry 70394
// log entry 17552
// log entry 26926
// log entry 33200
// log entry 7132
// log entry 84155
// log entry 15396
// log entry 85001
// log entry 97521
// log entry 28731
// log entry 81317
// log entry 16114
// log entry 67989
// log entry 25439
// log entry 87916
// log entry 38053
// log entry 30186
// log entry 51212
// log entry 79918
// log entry 29296
// log entry 3043
// log entry 82815
// log entry 87027
// log entry 90268
// log entry 83773
// log entry 95715
// log entry 13277
// log entry 42036
// log entry 58473
// log entry 27568
// log entry 55030
// log entry 40547
// log entry 97000
// log entry 25362
// log entry 5339
// log entry 52925
// log entry 75557
// log entry 84899
// log entry 2356
// log entry 87870
// log entry 20363
// log entry 88009
// log entry 86952
// log entry 24360
// log entry 27291
// log entry 25922
// log entry 59070
// log entry 66434
// log entry 79504
// log entry 35324
// log entry 16461
// log entry 60832
// log entry 24722
// log entry 96438
// log entry 14722
// log entry 29260
// log entry 42085
// log entry 87805
// log entry 55692
// log entry 47831
// log entry 85678
// log entry 31328
// log entry 91372
// log entry 70813
// log entry 31489
// log entry 59355
// log entry 15874
// log entry 32787
// log entry 78244
// log entry 12943
// log entry 45359
// log entry 15089
// log entry 37307
// log entry 56844
// log entry 99278
// log entry 113
// log entry 17739
// log entry 70430
// log entry 87545
// log entry 58642
// log entry 83108
// log entry 42575
// log entry 98718
// log entry 31907
// log entry 27911
// log entry 52912
// log entry 21109
// log entry 94401
// log entry 59197
// log entry 33618
// log entry 3932
// log entry 7210
// log entry 64126
// log entry 26566
// log entry 48355
// log entry 19560
// log entry 85391
// log entry 61552
// log entry 48766
// log entry 29397
// log entry 65633
// log entry 44500
// log entry 97421
// log entry 63701
// log entry 65463
// log entry 4679
// log entry 33476
// log entry 14157
// log entry 74749
// log entry 89004
// log entry 13881
// log entry 45838
// log entry 88887
// log entry 18144
// log entry 65942
// log entry 48644
// log entry 39980
// log entry 46443
// log entry 10653
// log entry 48228
// log entry 3840
// log entry 31188
// log entry 82928
// log entry 45430
// log entry 87213
// log entry 75750
// log entry 36316
// log entry 42155
// log entry 3596
// log entry 31241
// log entry 87629
// log entry 85813
// log entry 19649
// log entry 27683
// log entry 28644
// log entry 7567
// log entry 37816
// log entry 40775
// log entry 7001
// log entry 62728
// log entry 3703
// log entry 1828
// log entry 34218
// log entry 94010
// log entry 60925
// log entry 94811
// log entry 59390
// log entry 95766
// log entry 3345
// log entry 26272
// log entry 20657
// log entry 49617
// log entry 12323
// log entry 49980
// log entry 26537
// log entry 29529
// log entry 36237
// log entry 76681
// log entry 28650
// log entry 961
// log entry 67485
// log entry 49146
// log entry 55887
// log entry 90511
// log entry 85574
// log entry 23071
// log entry 9116
// log entry 23823
// log entry 66489
// log entry 85035
// log entry 42082
// log entry 51022
// log entry 9308
// log entry 55345
// log entry 59282
// log entry 84203
// log entry 13026
// log entry 13386
// log entry 75566
// log entry 81253
// log entry 177
// log entry 15198
// log entry 28572
// log entry 51233
// log entry 64682
// log entry 23615
// log entry 7610
// log entry 96112
// log entry 91847
// log entry 70605
// log entry 62251
// log entry 72693
// log entry 11854
// log entry 32256
// log entry 341
// log entry 33203
// log entry 92039
// log entry 51931
// log entry 54887
// log entry 6456
// log entry 6471
// log entry 21404
// log entry 3913
// log entry 11415
// log entry 28836
// log entry 29725
// log entry 31398
// log entry 82159
// log entry 79280
// log entry 10847
// log entry 65040
// log entry 89908
// log entry 91217
// log entry 97389
// log entry 68771
// log entry 13964
// log entry 3112
// log entry 98241
// log entry 76298
// log entry 66714
// log entry 13943
// log entry 25795
// log entry 36490
// log entry 40341
// log entry 98365
// log entry 41656
// log entry 40347
// log entry 2737
// log entry 8358
// log entry 46179
// log entry 86745
// log entry 702
// log entry 31428
// log entry 48928
// log entry 10710
// log entry 117
// log entry 68380
// log entry 88569
// log entry 67427
// log entry 64884
// log entry 7817
// log entry 16048
// log entry 7971
// log entry 94760
// log entry 92084
// log entry 17590
// log entry 39878
// log entry 49342
// log entry 47149
// log entry 52988
// log entry 10994
// log entry 11023
// log entry 72518
// log entry 29972
// log entry 19546
// log entry 63899
// log entry 1752
// log entry 20295
// log entry 26754
// log entry 3363
// log entry 2716
// log entry 21638
// log entry 81638
// log entry 55442
// log entry 73324
// log entry 97700
// log entry 69761
// log entry 60027
// log entry 65716
// log entry 37092
// log entry 32485
// log entry 84606
// log entry 6616
// log entry 82646
// log entry 37912
// log entry 91772
// log entry 12068
// log entry 12169
// log entry 61065
// log entry 27999
// log entry 72754
// log entry 13695
// log entry 90111
// log entry 87086
// log entry 22673
// log entry 55488
// log entry 48042
// log entry 4672
// log entry 60248
// log entry 39915
// log entry 89455
// log entry 40834
// log entry 52993
// log entry 26973
// log entry 74575
// log entry 90291
// log entry 76025
// log entry 20397
// log entry 12804
// log entry 37696
// log entry 11334
// log entry 70867
// log entry 6126
// log entry 5973
// log entry 53419
// log entry 83036
// log entry 21818
// log entry 24618
// log entry 6062
// log entry 38184
// log entry 20310
// log entry 57005
// log entry 53004
// log entry 62756
// log entry 31079
// log entry 34315
// log entry 77122
// log entry 18676
// log entry 65981
// log entry 36029
// log entry 42026
// log entry 87850
// log entry 48899
// log entry 80341
// log entry 23072
// log entry 64129
// log entry 97972
// log entry 14147
// log entry 33569
// log entry 90126
// log entry 89463
// log entry 221
// log entry 67561
// log entry 15550
// log entry 99637
// log entry 32655
// log entry 96096
// log entry 91520
// log entry 73126
// log entry 31247
// log entry 47371
// log entry 47763
// log entry 77263
// log entry 39053
// log entry 87237
// log entry 61951
// log entry 705
// log entry 57299
// log entry 84831
// log entry 70999
// log entry 34995
// log entry 92233
// log entry 64140
// log entry 3259
// log entry 54159
// log entry 46874
// log entry 72427
// log entry 5154
// log entry 21450
// log entry 64582
// log entry 35170
// log entry 30565
// log entry 5002
// log entry 76391
// log entry 38707
// log entry 96066
// log entry 78315
// log entry 66698
// log entry 13021
// log entry 79297
// log entry 39277
// log entry 50136
// log entry 54531
// log entry 20854
// log entry 30774
// log entry 54281
// log entry 52040
// log entry 66790
// log entry 40645
// log entry 33753
// log entry 15816
// log entry 58805
// log entry 4970
// log entry 73112
// log entry 23675
// log entry 58536
// log entry 26701
// log entry 38552
// log entry 72359
// log entry 80105
// log entry 67381
// log entry 24115
// log entry 12095
// log entry 57922
// log entry 82222
// log entry 3828
// log entry 21045
// log entry 13601
// log entry 25258
// log entry 18483
// log entry 42103
// log entry 88468
// log entry 1557
// log entry 60670
// log entry 24841
// log entry 92396
// log entry 27138
// log entry 62380
// log entry 53055
// log entry 79391
// log entry 91796
// log entry 33845
// log entry 46027
// log entry 7390
// log entry 19737
// log entry 42541
// log entry 87165
// log entry 28979
// log entry 40885
// log entry 7294
// log entry 91666
// log entry 43338
// log entry 92196
// log entry 81404
// log entry 25312
// log entry 25780
// log entry 10335
// log entry 65460
// log entry 1190
// log entry 53370
// log entry 11470
// log entry 73312
// log entry 37224
// log entry 28321
// log entry 23459
// log entry 53764
// log entry 32237
// log entry 92787
// log entry 1197
// log entry 49325
// log entry 22604
// log entry 61332
// log entry 98174
// log entry 55080
// log entry 46938
// log entry 87656
// log entry 68141
// log entry 45827
// log entry 78241
// log entry 72691
// log entry 39911
// log entry 51562
// log entry 59102
// log entry 63213
// log entry 27408
// log entry 28986
// log entry 42994
// log entry 41986
// log entry 19768
// log entry 28893
// log entry 22396
// log entry 92248
// log entry 73161
// log entry 5786
// log entry 35059
// log entry 67362
// log entry 7756
// log entry 24420
// log entry 50919
// log entry 8222
// log entry 58180
// log entry 11203
// log entry 74492
// log entry 27714
// log entry 86415
// log entry 57041
// log entry 77360
// log entry 98053
// log entry 28318
// log entry 16574
// log entry 88720
// log entry 54338
// log entry 71870
// log entry 84012
// log entry 43985
// log entry 79983
// log entry 44038
// log entry 50634
// log entry 36267
// log entry 3597
// log entry 78528
// log entry 72602
// log entry 28323
// log entry 97082
// log entry 70447
// log entry 28776
// log entry 2069
// log entry 98992
// log entry 86969
// log entry 9556
// log entry 56540
// log entry 79128
// log entry 48388
// log entry 63064
// log entry 42919
// log entry 89881
// log entry 28512
// log entry 23486
// log entry 44258
// log entry 99107
// log entry 35289
// log entry 12749
// log entry 73278
// log entry 86084
// log entry 85837
// log entry 88688
// log entry 99299
// log entry 78374
// log entry 56537
// log entry 53145
// log entry 15464
// log entry 27848
// log entry 58669
// log entry 27664
// log entry 57626
// log entry 65386
// log entry 77507
// log entry 88257
// log entry 52058
// log entry 28250
// log entry 26670
// log entry 54272
// log entry 11865
// log entry 30568
// log entry 83972
// log entry 61199
// log entry 73574
// log entry 56705
// log entry 9685
// log entry 55244
// log entry 83994
// log entry 6346
// log entry 45458
// log entry 50168
// log entry 55978
// log entry 24613
// log entry 12974
// log entry 37805
// log entry 31138
// log entry 78124
// log entry 52550
// log entry 25049
// log entry 17244
// log entry 41660
// log entry 20568
// log entry 55021
// log entry 93268
// log entry 10694
// log entry 5866
// log entry 34126
// log entry 65231
// log entry 93664
// log entry 11546
// log entry 91348
// log entry 35678
// log entry 92674
// log entry 6106
// log entry 60378
// log entry 51446
// log entry 36433
// log entry 66693
// log entry 67537
// log entry 75639
// log entry 91150
// log entry 86443
// log entry 90488
// log entry 33395
// log entry 79134
// log entry 31374
// log entry 90443
// log entry 75871
// log entry 78926
// log entry 69023
// log entry 42593
// log entry 79551
// log entry 34424
// log entry 92755
// log entry 27196
// log entry 58940
// log entry 71991
// log entry 55558
// log entry 19743
// log entry 80262
// log entry 49465
// log entry 31001
// log entry 58559
// log entry 48751
// log entry 4498
// log entry 68052
// log entry 16866
// log entry 22344
// log entry 45346
// log entry 2995
// log entry 57391
// log entry 78761
// log entry 99679
// log entry 64277
// log entry 77073
// log entry 49488
// log entry 51075
// log entry 69331
// log entry 29964
// log entry 86727
// log entry 76823
// log entry 52653
// log entry 43869
// log entry 92359
// log entry 63725
// log entry 66719
// log entry 4339
// log entry 68084
// log entry 21451
// log entry 28662
// log entry 11265
// log entry 55451
// log entry 29161
// log entry 47139
// log entry 92987
// log entry 6598
// log entry 84535
// log entry 88987
// log entry 95519
// log entry 59676
// log entry 12068
// log entry 7429
// log entry 34282
// log entry 91631
// log entry 25137
// log entry 93443
// log entry 50122
// log entry 96119
// log entry 99179
// log entry 17167
// log entry 8454
// log entry 60444
// log entry 36275
// log entry 3979
// log entry 60342
// log entry 25037
// log entry 90208
// log entry 55852
// log entry 22726
// log entry 2990
// log entry 67163
// log entry 30927
// log entry 67119
// log entry 62561
// log entry 22324
// log entry 64614
// log entry 1546
// log entry 87227
// log entry 51676
// log entry 79296
// log entry 19244
// log entry 99078
// log entry 29400
// log entry 70757
// log entry 15472
// log entry 34509
// log entry 44709
// log entry 69450
// log entry 4765
// log entry 67377
// log entry 15933
// log entry 12413
// log entry 3327
// log entry 23597
// log entry 70724
// log entry 72200
// log entry 77732
// log entry 86318
// log entry 78692
// log entry 25962
// log entry 10783
// log entry 77911
// log entry 38983
// log entry 86288
// log entry 51915
// log entry 72039
// log entry 85655
// log entry 79242
// log entry 84017
// log entry 48362
// log entry 4560
// log entry 25298
// log entry 31975
// log entry 92576
// log entry 32995
// log entry 91016
// log entry 92517
// log entry 5672
// log entry 59781
// log entry 7922
// log entry 59369
// log entry 16432
// log entry 93803
// log entry 70623
// log entry 80273
// log entry 61434
// log entry 63946
// log entry 48176
// log entry 31923
// log entry 12969
// log entry 16735
// log entry 45722
// log entry 78352
// log entry 1368
// log entry 94738
// log entry 28410
// log entry 3188
// log entry 5985
// log entry 67484
// log entry 57312
// log entry 8269
// log entry 94886
// log entry 79436
// log entry 32186
// log entry 55499
// log entry 65473
// log entry 87614
// log entry 44239
// log entry 5802
// log entry 70865
// log entry 24128
// log entry 57028
// log entry 94562
// log entry 6196
// log entry 65445
// log entry 96242
// log entry 40800
// log entry 75894
// log entry 72748
// log entry 7557
// log entry 90141
// log entry 11977
// log entry 91503
// log entry 95983
// log entry 70674
// log entry 3844
// log entry 28669
// log entry 28155
// log entry 84226
// log entry 37339
// log entry 33111
// log entry 56372
// log entry 52808
// log entry 68162
// log entry 88086
// log entry 73917
// log entry 3542
// log entry 97091
// log entry 70539
// log entry 73698
// log entry 16797
// log entry 3953
// log entry 36234
// log entry 86963
// log entry 23502
// log entry 50580
// log entry 33661
// log entry 63456
// log entry 11156
// log entry 5108
// log entry 97124
// log entry 6888
// log entry 89752
// log entry 22407
// log entry 69950
// log entry 90648
// log entry 78714
// log entry 91335
// log entry 60767
// log entry 27134
// log entry 89016
// log entry 68247
// log entry 22811
// log entry 40035
// log entry 21980
// log entry 55199
// log entry 59549
// log entry 12450
// log entry 89789
// log entry 19435
// log entry 61686
// log entry 62299
// log entry 49648
// log entry 52103
// log entry 89388
// log entry 18826
// log entry 67220
// log entry 3575
// log entry 37902
// log entry 97373
// log entry 59423
// log entry 64513
// log entry 79372
// log entry 36331
// log entry 29354
// log entry 39406
// log entry 492
// log entry 39533
// log entry 50878
// log entry 49606
// log entry 47638
// log entry 69219
// log entry 1783
// log entry 65400
// log entry 17025
// log entry 85556
// log entry 32968
// log entry 50637
// log entry 67280
// log entry 99759
// log entry 97081
// log entry 46511
// log entry 33842
// log entry 51389
// log entry 96993
// log entry 13492
// log entry 57510
// log entry 27889
// log entry 16456
// log entry 23226
// log entry 17548
// log entry 99700
// log entry 7689
// log entry 38420
// log entry 34250
// log entry 46822
// log entry 2240
// log entry 1817
// log entry 3849
// log entry 72514
// log entry 9994
// log entry 82838
// log entry 88177
// log entry 39050
// log entry 36137
// log entry 78144
// log entry 16648
// log entry 2245
// log entry 14497
// log entry 7350
// log entry 13732
// log entry 29324
// log entry 70396
// log entry 25737
// log entry 97716
// log entry 29980
// log entry 89603
// log entry 88868
// log entry 97783
// log entry 46967
// log entry 17721
// log entry 18310
// log entry 12918
// log entry 41186
// log entry 92710
// log entry 66182
// log entry 97256
// log entry 84618
// log entry 28160
// log entry 1987
// log entry 37424
// log entry 80181
// log entry 42776
// log entry 39178
// log entry 91424
// log entry 20026
// log entry 90081
// log entry 5791
// log entry 81718
// log entry 78244
// log entry 63320
// log entry 23908
// log entry 780
// log entry 7492
// log entry 82578
// log entry 87341
// log entry 1845
// log entry 53930
// log entry 40903
// log entry 95844
// log entry 66206
// log entry 36101
// log entry 35810
// log entry 33262
// log entry 60184
// log entry 70158
// log entry 21799
// log entry 50787
// log entry 36437
// log entry 24452
// log entry 7936
// log entry 42197
// log entry 44306
// log entry 87243
// log entry 37074
// log entry 942
// log entry 60777
// log entry 29460
// log entry 48170
// log entry 11056
// log entry 10759
// log entry 66748
// log entry 64015
// log entry 40881
// log entry 13210
// log entry 61325
// log entry 96610
// log entry 82277
// log entry 65380
// log entry 33180
// log entry 69318
// log entry 91277
// log entry 25896
// log entry 83710
// log entry 17182
// log entry 50539
// log entry 35693
// log entry 22637
// log entry 84177
// log entry 82667
// log entry 81276
// log entry 35609
// log entry 57936
// log entry 97281
// log entry 55636
// log entry 44457
// log entry 90635
// log entry 57396
// log entry 40498
// log entry 9059
// log entry 87325
// log entry 41745
// log entry 57421
// log entry 12100
// log entry 83183
// log entry 88477
// log entry 20945
