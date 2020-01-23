using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Account_Information
{
    static class Program
    {

        private class AccountData
        {
            public string id { get; set; }
            public string username { get; set; }
            public string discriminator { get; set; }
            public string email { get; set; }
            public string verified { get; set; }
            public string locale { get; set; }
            public string mfa_enabled { get; set; }
            public string phone { get; set; }
            public string flags { get; set; }
        }

        [STAThread]
        static void Main()
        {
            string Token = "1";
            HttpWebRequest httpWebRequest = (HttpWebRequest)WebRequest.Create("https://discordapp.com/api/v6/users/@me");
            httpWebRequest.ContentType = "application/json; charset=utf-8";
            httpWebRequest.Method = "GET";
            httpWebRequest.Headers["Authorization"] = Token;
            HttpWebResponse httpWebResponce = (HttpWebResponse)httpWebRequest.GetResponse();
            if (httpWebResponce.StatusCode.ToString() == "OK")
            {
                Stream DataStream = httpWebResponce.GetResponseStream();
                StreamReader Reader = new StreamReader(DataStream);
                string RawData = Reader.ReadToEnd();
                AccountData data = JsonConvert.DeserializeObject<AccountData>(RawData);
                var IDbox = data.id;
                var TAGbox = data.username + "#" + data.discriminator;
                var EMAILbox = data.email;
                var VERIFIEDbox = data.verified;
                var LANGUAGEbox = data.locale;
                var AUTHbox = data.mfa_enabled;
                var PHONEbox = data.phone;
                var FLAGbox = data.flags;
            }
            else
            {
                MessageBox.Show("Problem speaking with the discord account api.");
            }
        }
    }
}
