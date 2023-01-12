public class Solution {
    public IList<IList<string>> FindDuplicate(string[] paths) {
        IList<IList<string>> retList = new List<IList<string>>();
        Dictionary<string, List<string>> contentAndFiles = new Dictionary<string, List<string>>();
        
        foreach(string p in paths) {
            string[] pathAndFiles = p.Split(' ');
            string path = pathAndFiles[0];
            List<string> files = pathAndFiles.Skip(1).ToList();
            foreach(string file in files) {
                int fileContentStartIndex = file.IndexOf('(') + 1;
                string fileContent = file.Substring(fileContentStartIndex, file.Length - fileContentStartIndex - 1);
                string filePath = path + "/" + file.Substring(0, fileContentStartIndex - 1);
                if (!contentAndFiles.ContainsKey(fileContent)) {
                    contentAndFiles[fileContent] = new List<string>{filePath};
                } else {
                    contentAndFiles[fileContent].Add(filePath);
                }
            }
        }
        
        foreach(KeyValuePair<string, List<string>> entry in contentAndFiles) {
            if (entry.Value.Count() > 1) {
                retList.Add(entry.Value);
            }
        }
        
        return retList;
    }
}