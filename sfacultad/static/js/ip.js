function validar(){
  
    var ip = document.getElementById('ip');
    var extra=ip.value;
    var o1 = extra.split('.',1);
    var o2 = extra.split('.',2);
    var o2 = o2[1];
    var ipformat = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
    var PoP="publica";
    var clase="xx";



    if(ip.value.match(ipformat))
    {   
        var vali = document.getElementById('Validacion');
        vali.innerHTML = 'Ip validada';
        if (o1 <= 127){
            if (o1 == 10 ) {
                PoP="Privada";           //clase a privada
            }
            clase=" Clase A";
        }

        if (o1 > 127 && o1 <192){
            if (o1 == 172 && (o2 >=16 && o2 <=31))  {
                PoP="Privada";
          //clase b privada
            }
            clase="Clase B";
        }

        if (o1 == 127){
            PoP="Loopback";
            clase="Clase A";
        }


        if (o1 == 192 && o1<=223){
            if (o1 == 192 && o2 ==168)  {
                PoP="Privada";
           //clase c privada
            }
            clase="Clase C";
        }


        var pop = document.getElementById('PoP');
        pop.innerHTML = PoP;

        var cl = document.getElementById('Clase');
        cl.innerHTML = clase;
  

    }
else{
    alert("no es valida");

}
}

