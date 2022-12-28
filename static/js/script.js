function plus(){
    btnPlus = document.getElementById("plus");
    textFeild = document.getElementById("plot-size");
    if(textFeild.value == ""){
        start = 0.0;
    }else{
        start = parseFloat(textFeild.value);
    }
    textFeild.value =(start + 1).toFixed(1);
}

function minus(){
    btnMinus = document.getElementById("minus");
    textFeild = document.getElementById("plot-size");
    if(textFeild.value == "" || textFeild.value == 0.0){
        return
    }else{
        start = parseFloat(textFeild.value);
        if((start - 1) < 0.0){
            textFeild.value = (0.0).toFixed(1); 

            return
        }
    }
    textFeild.value =(start - 1).toFixed(1);
}

function calculate(){
    dap = 88 * textFeild.value;
    mop = 67 * textFeild.value;
    urea = 142 * textFeild.value;
    document.getElementById("dap").innerHTML = "Dap " + dap+"kg";
    document.getElementById("mop").innerHTML = "Mop " + mop+"kg";
    document.getElementById("urea").innerHTML = "Urea " + urea+"kg";
}