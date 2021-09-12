
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




let previousMinutes;

const checkTime = function() {
    const currentTime = new Date();
    const hour = currentTime.getHours();
      if (hour ==18) {var n = new Notification("Hello World")};

};


Notification.onclick = function(event) {
  event.preventDefault();
  window.open(https://sites.google.com/view/laretech-lecture/%E3%83%9B%E3%83%BC%E3%83%A0)
}


//その日の問題のノルマを特定時間までに完了していない場合に通知を送る。→webの操作履歴が必要？、History API　問題をやっていない場合、windowsの更新画面位の頻度で通知が来る
