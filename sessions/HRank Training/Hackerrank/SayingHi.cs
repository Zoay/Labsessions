using System;
using System.IO;
using System.Text.RegularExpressions;

namespace Hackerrank.SayingHi
{
	public class SayingHi
	{
		public SayingHi ()
		{
		}

		public string SayHi()
		{
			string result = "";
			string filename = @"/Applications/MAMP/htdocs/Zoay/Labsessions/sessions/HRank Training/Hackerrank/sayhi.txt";

			using (TextReader tr = new StreamReader (new FileStream (filename, FileMode.Open))) {
				int n = Convert.ToInt32 (tr.ReadLine ());
				string pattern = @"^(hi)\s[^d].";
				Regex _regex = new Regex (pattern, RegexOptions.IgnoreCase);

				if (1 <= n && n <= 10) {
					string line;
					while ((line = tr.ReadLine ()) != null) {
						string[] words = line.Split (' ');
						int wordCounter = words.Length;

						if (1 <= wordCounter && wordCounter <= 10) {
							Match m = _regex.Match (line);
							if (m.Success) {
								result += line + "\n";
							}
						}
					}
				}
			}
			return result;
		}

		public static void main(String[] args)
		{
			Console.WriteLine (new SayingHi ().SayHi ());
		}
	}
}

