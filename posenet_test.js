// init function
async function init(){

    //posenet 모델 불러오기
    model =  await tf.loadModel('https://unpkg.com/@tensorflow-models/posenet');
    


    //-----------------수정------------------------
    //모델 로드 AI가 플레이함
    console.log('model loaded from storage');
    computer.ai_plays = true;

    if(computer.ai_plays){
        document.getElementById("playing").innerHTML = "Playing: AI";
    }else{
        document.getElementById("playing").innerHTML = "Playing: Computer";
    }

    // start a game 게임시작
    animate(step);
}