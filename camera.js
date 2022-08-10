

//querySelector란?
//https://velog.io/@chloeee/getElementById-%EA%B7%B8%EB%A6%AC%EA%B3%A0-querySelector-%EC%B0%A8%EC%9D%B4%EC%A0%90
//
let constraints = { video: { facingMode: "user"}, audio: false};
const cameraView = document.querySelector("#camera--view");     
const cameraOutput = document.querySelector("#camera--output"); 
const cameraSensor = document.querySelector("#camera--sensor"); 
const cameraTrigger = document.querySelector("#camera--trigger");



//시작 함수
function cameraStart(){

    // MediaDevices.getUserMedia 
    // 사용자에게 미디어 입력 장치 사용 권한을 요청 -> MediaStream (en-US)을 반환
    // https://developer.mozilla.org/ko/docs/Web/API/MediaDevices/getUserMedia

    navigator.mediaDevices.getUserMedia(constraints)
        .then(function(stream){
            //stream을 받아서 해당 스트림이 트랙을 받아 track 변수에 할당
            track = stream.getTracks()[0];
            cameraView.srcObject = stream;

        })
        .catch(function(error){
            console.error("카메라에 문제가 있습니다.", error);
        })
}

function camera_detect(){


}



//촬영 버튼 클릭 리스너
cameraTrigger.addEventListener("click", function(){
    
    //camera 뷰 크기 설정 (640)
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);

    //결과
    cameraOutput.src = cameraSensor.toDataURL("image/webp");
    cameraOutput.classList.add("taken");

    //log
    console.log(cameraSensor.height);

});

// 페이지가 로드되면 함수 실행
window.addEventListener("load", cameraStart, false);