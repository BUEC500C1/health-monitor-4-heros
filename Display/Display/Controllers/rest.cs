using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.IO;

namespace Display.Controllers {
    [ApiController]
    [Route("/")]
    public class Rest : ControllerBase {


        [HttpGet("{requestName}")]
        public async Task<string> Get(string requestName) {
            return await Task.Run(() => {
                return JsonSerializer.Serialize(new {
                    name = requestName,
                    status = "running",
                    timeStamp = (DateTime.UtcNow-DateTime.UnixEpoch).TotalSeconds.ToString()
                });
            });
        }
        [HttpPost("{requestName}")]
        public async Task<string> Post(string requestName) {
            string resquestInfoJson;
            using (var reader = new StreamReader(Request.Body)) {
                resquestInfoJson = await reader.ReadToEndAsync();
            }
            var processorInfo = JsonSerializer.Deserialize<Dictionary<string, string>>(resquestInfoJson);
            switch (requestName) {
                case ("spo2"):
                    Display.MainWindow.data.OxygenCurrent = processorInfo["value"];
                    break;
                case ("awrr"):
                    Display.MainWindow.data.AwRR = processorInfo["value"];
                    break;
                case ("bp"):
                    Display.MainWindow.data.BloodPressure = processorInfo["value"];
                    break;
                case ("hr"):
                    Display.MainWindow.data.HeartRateCurrent = processorInfo["value"];
                    break;
                default:
                    return await Task.Run(() => {
                        return JsonSerializer.Serialize(new {
                            error="error"
                        });
                    });
            }
            return await Task.Run(() => {
                return JsonSerializer.Serialize(new {
                    ok = "ok"
                });
            });
        }
    }
}
