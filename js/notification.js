
window.onload = function() {
   Notification.requestPermission();
   setInterval(checkTime, 6000);    //現在10分ごとのプログラム、本番では6倍にすること
};
Notification.requestPermission(function(result) {
    if (result === 'denied') {
      alert('リクエスト結果：通知許可されませんでした');
    } else if (result === 'default') {
      alert('リクエスト結果：通知可能か不明です');
    } else if (result === 'granted') {
      alert('リクエスト結果：通知許可されました！！');
    }
  })

const checkTime = function() {
    const currentTime = new Date();
    const hour = currentTime.getHours();
      if (hour ==22) {var greet = new Notification("Hello World")};
      greet.addEventListener('click',function(){
        window.open('https://www.youtube.com/watch?v=ufKn_OXBbYI');
      });

};


//その日の問題のノルマを特定時間までに完了していない場合に通知を送る。→webの操作履歴が必要？、History API　問題をやっていない場合、windowsの更新画面位の頻度で通知が来る
