var sol = '{{solArr}}';
var err = '{{errArr}}';
sol = sol.replace('[','');
sol = sol.replace('])','');
err = err.replace('[','');
err = err.replace('])','');
let solArr = sol.split (',');
let errArr = err.split (',');
solArr.shift();
errArr.shift();


var table =
'<table><thead><tr><th>Số lần lặp</th><th>Nghiệm x</th><th>Sai số</th></tr></thead><tbody></tbody>';

for (var i = 0; i < solArr.length; i++) {  
    table += '<tr><td>' + (i + 1) + '</td><td>' + solArr[i] + '</td><td>' + errArr[i] + '</td></tr>';
}
table += '</tbody></table>';
document.getElementById("text-table").innerHTML = table;