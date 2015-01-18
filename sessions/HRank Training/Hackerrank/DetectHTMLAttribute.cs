using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Collections.Generic;

namespace Hackerrank.DetectHTMLAttribute
{
	public class DetectHTMLAttribute
	{
		public static void main(string[] args)
		{
			Console.WriteLine (new DetectHTMLAttribute ().DetectHTMLAttributes ());
		}

		public string DetectHTMLAttributes()
		{
			string filename1 = @"/Applications/MAMP/htdocs/Zoay/Labsessions/sessions/HRank Training/Hackerrank/detectHTMLAttribute1.txt";
			//string filename2 = @"/Applications/MAMP/htdocs/Zoay/Labsessions/sessions/HRank Training/Hackerrank/detectHTMLAttribute2.txt";

			string sTag = @"([a-z]+)";
			string dotplus = "\".+\"";
			string sAttr = @"(([a-z]+)=" + dotplus + ")*";

			string pattern = @"(<" + sTag + @"\s?" + sAttr + @">)*";
			Regex _regex = new Regex (pattern, RegexOptions.IgnoreCase);

			//List<string> HTMLAttributes = new List<string> ();

			using (TextReader tr = new StreamReader (new FileStream (filename1, FileMode.Open))) {
				int n = Convert.ToInt32 (tr.ReadLine ());
				int count = 0;
				string line;
				while ((line = tr.ReadLine ()) != null) {
					Match m = _regex.Match(line);

					MatchCollection mc = _regex.Matches (line);

					/*if(m.Success) {

						Console.WriteLine ("Matching Ok!");
					}*/


					if(mc.Count>0) {

						Console.WriteLine ("Matching Ok!");
					}


					count++;
				}
				Console.WriteLine ("count {0}", count.ToString());
			}
			return "";
		}
	}
}

