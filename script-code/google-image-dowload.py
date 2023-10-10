# from google_images_download import google_images_download
#
# #instantiate the class
# response = google_images_download.googleimagesdownload()
# arguments = {"keywords":"reflective_coveralls",
#              "limit":400,
#              "print_urls": False
#              # "chromedriver":"C:\\Users\\selca\\Selcan_Atak\\File\\Code\\Python-script-code\\chromedriver.exe",
#              }
# paths = response.download(arguments)
#
# #print complete paths to the downloaded images
# print(paths)


#####################################
#Bing
from bing_image_downloader import downloader
downloader.download("Wearing a helmet at work", limit=300,  output_dir='baret',
                    adult_filter_off=True, force_replace=False, timeout=60)