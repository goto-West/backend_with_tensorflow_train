
const fs = require('fs');
const path = require('path');
const process = require('process');
const tf = require('@tensorflow/tfjs-node');


const modelpath = 'file://model_NBC.sav';

// main function
async function main() {

    //load classification model
    await tf.enableProdMode();
    await tf.setBackend('tensorflow');
    await tf.ENV.set('DEBUG', false);
    await tf.ready();
    model =  await tf.loadModel(modelpath);
    

    // 
    const res = model.execute(img.tensor);
    
}