$(document).ready(function() {
    
    var TABLE1_STRIDE = 1;
    var TABLE1_BYTES = 3;
    var probeTable = ['alpha', 'beta', 'corky'];
    var simpleByteArray = [0x00, 0x01, 0x02];
    var localJunk;
    var index = 0;
    if (index < simpleByteArray.length) {
        index = simpleByteArray[index | 0];
        index = (((index * TABLE1_STRIDE) | 0) & (TABLE1_BYTES - 1)) | 0;
        localJunk &= probeTable[index | 0] | 0;
    }
    console.log(localJunk);
    $('#text').text(localJunk);
    
});
