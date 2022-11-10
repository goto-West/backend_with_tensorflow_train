//const fs = require('fs');
//const path = require('path');
//const process = require('process');

var spawn = require('child_process').spawn;

// main function
async function main() {

    let argument = [[160, 145, 176, 164, 112, 72, 176, 176]];

    console.log("workings in js");
    //load python 
    const pythonClassification = spawn('python', ['model_test.py',argument]);
    
    //pid number
    console.log(pythonClassification.pid.toString());

    pythonClassification.stdout.on('data', function(data) {
        console.log(data.toString());
    })  
    
    pythonClassification.stderr.on('data', function(data) {
        console.log(data.toString());
        
    })  
    
    /*
    pythonClassification.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    pythonClassification.on('data', (data) => {
        console.log(`error:${data}`);
    });
    
    pythonClassification.on('exit', () => {
        console.log(`Classification process ended with code`);
    });
    /*
    $.ajax({
        type: "POST",
        url: "~/model_classification.py",
        data: { param: text}
      }).done(function( o ) {
         
    });
    */
    
}

main();

