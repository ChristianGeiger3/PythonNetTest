

namespace DownloadFile;

public class DownloadWorker
{

   public void Download(Uri completeUrl)
        {
            Console.WriteLine("DASF: Start");
            var httpClient = new HttpClient();

            var request = new HttpRequestMessage(HttpMethod.Get, completeUrl);
           
            HttpResponseMessage response;
          
            Console.WriteLine("DASF: send ...");
            response = httpClient.Send(request);
    
            Console.WriteLine($"DASF: response --> {response.StatusCode}");
            if (response.StatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"DASF: successful");
            }
            else
            {
                throw new InvalidDataException($"The response code ist not ok. Response code: {response.StatusCode}");
            }
        }
}
