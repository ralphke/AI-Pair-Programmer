using System;
using System.Collections.Generic;
using System.Xml;
using Newtonsoft.Json;
using System.IO;

public class XmlToJsonConverter
{
    public static void ConvertXML()
    {
        string inputXmlString = "<?xml version=\"1.0\"?>\r\n<feedback xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\r\n  <version>1.0</version>\r\n  <report_metadata>\r\n    <org_name>Enterprise Copilot</org_name>\r\n    <email>copilot@openai.com</email>\r\n    <report_id>e0381c24b5234bed3hdl0hk2b5c944d0b6</report_id>\r\n    <date_range>\r\n      <begin>1711238400</begin>\r\n      <end>1711324800</end>\r\n    </date_range>\r\n  </report_metadata>\r\n  <policy_published>\r\n    <domain>openai.com</domain>\r\n    <adkim>s</adkim>\r\n    <aspf>r</aspf>\r\n    <p>none</p>\r\n    <sp>none</sp>\r\n    <pct>100</pct>\r\n    <fo>0</fo>\r\n  </policy_published>\r\n</feedback>";
        string outputFilePath = "output.json";
        XmlToJsonConverter converter = new XmlToJsonConverter();
        ConvertXmlToJson(inputXmlString, outputFilePath);
    }

    public static void ConvertXmlToJson(string inputXmlString, string outputFilePath)
    {
        try
        {
            XmlDocument doc = new XmlDocument();
            doc.LoadXml(inputXmlString);
            string jsonText = JsonConvert.SerializeXmlNode(doc);
            File.WriteAllText(outputFilePath, jsonText);
        }
        catch (XmlException)
        {
            Console.WriteLine($"Error: {inputXmlString} is not a well-formed XML document.");
        }
        catch (IOException)
        {
            Console.WriteLine($"Error: Unable to write to {outputFilePath}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Unexpected error: {e.Message}");
        }
    }
}