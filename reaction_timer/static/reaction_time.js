var startTime;
var reactionTime;
var i = 5;

const timer = document.getElementById("timer");
const question = document.getElementById("question");
const reaction = document.getElementById("reaction");
console.log(CSRF_TOKEN);

var Interval = setInterval(function(){
  timer.innerHTML = i;
  i--;

  if (i<=0){

    timer.innerHTML = "Select what applies:";
    startTime = Date.now()
    question.style.display = 'inline';
    reaction.onclick = function(){
      reactionTime = Date.now()-startTime;
      reaction.disabled = true;
      }

    axios({
      method:'post',
      url:PAGE_URL, 
      data:{'reaction_time':reactionTime.toString()},
      headers:{'X-CSRFToken':CSRF_TOKEN,
              "content-type": "application/json"}
    }
    ).then(res => console.log(res))
    .catch(err => console.log(err))
    clearInterval(Interval);
    }
  }, 
  1750
)



 