from multiprocessing import Process
import sys
import unittest

import time
sys.path.append("/home/vagrant/Documents/PythonNetTest/DownloadFile/bin/Debug/net6.0")
from pythonnet import load
load("coreclr")
import clr

clr.AddReference("DownloadFile")

class DonwloadTests(unittest.TestCase):
  
     def test_download(self):

        # self.DoThread()
        
        self.DoProc()

     def DoThread(self):
         print("--Thread--")
         import threading
         thread = threading.Thread(target = self.DoWork)
         thread.start()
        #  thread.join()
         i = 0
         while thread.is_alive():
             print(f" {i} is alive: {thread.is_alive()} |")
             time.sleep(5)
             i=i+1

     def DoProc(self):
         print("--Process--")
         p = Process(target=self.DoWork)
       
         p.start()
        
         i = 0
         while p.is_alive():
             print(f" {i} | exitcode: {p.exitcode} | is alive: {p.is_alive()} |")
             time.sleep(5)
             i=i+1
             
         print(f" done proc --> exitcode: {p.exitcode} | is alive: {p.is_alive()} |")

     def DoWork(self):
       
        
         feedUrl = 'https://mp4-download.com/4k-MP4'
         from DownloadFile import DownloadWorker
         from System import Uri, Exception
            
         feedUri = Uri(str(feedUrl))
         worker = DownloadWorker()
         print("get_data: start get package")
         worker.Download(feedUri)
                
         print("done download ")   
   
if __name__ == '__main__':
    unittest.main()