function replace(x) {
  var text = String(x);

  var lines = text.split("\n");
  var returnedText="";

  for(i=0;i<lines.length;i++){
  	returnedText += lines[i].toString().allReplace({'É™': 'ə', 'Ä±': 'ı', 'Ã¶': 'ö', 'Ã¼': 'ü','Ã§': 'ç','Ä°': 'İ','ÄŸ': 'ğ','ÅŸ': 'ş', 'Æ': 'Ə','Åž': 'Ş'});
  	returnedText += "\n";
  }

  return returnedText;
}

String.prototype.allReplace = function(obj) {
    var retStr = this;
    for (var x in obj) {
        retStr = retStr.replace(new RegExp(x, 'g'), obj[x]);
    }
    return retStr;
};