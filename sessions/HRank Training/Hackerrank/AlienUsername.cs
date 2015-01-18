using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Collections.Generic;

namespace Hackerrank.AlienUsername
{
	public class AlienUsername
	{
		const string VALID = "VALID";
		const string INVALID = "INVALID";

		public AlienUsername ()
		{
		}

		public static void Main(string[] args)
		{
			//Console.WriteLine (new AlienUsername ().ValidAlienUsername ());
			new AlienUsername ().ValidAlienUsername ();
		}

		public void ValidAlienUsername()
		{
			Console.Write("Type the filename: ");
			string filename = Console.ReadLine ();
			List<string> results = new List<string> ();

			using (TextReader tr = new StreamReader (new FileStream (filename, FileMode.Open))) 
			{
				int n = Convert.ToInt32 (tr.ReadLine ());
				string pattern =  @"^[_|\.][0-9]+[a-zA-Z]+_?";
				Regex _regex = new Regex (pattern);

				if (1 <= n && n <= 100) 
				{
					string line;
					while ((line = tr.ReadLine ()) != null) 
					{
						Match m = _regex.Match (line);
						if (m.Success) 
						{
							results.Add (VALID);
						} 
						else 
						{
							results.Add (INVALID);
						}
					}
				}
			}

			foreach (string res in results)
			{
				Console.WriteLine (res);
			}
		}
	}
}

