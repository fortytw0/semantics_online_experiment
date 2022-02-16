var startTime;
var reactionTime;
var i = 5;
var isClicked = false;

const timer = document.getElementById("timer");
const question = document.getElementById("question");
const reaction = document.getElementById("reaction");
const antireaction = document.getElementById("anti-reaction");
console.log(CSRF_TOKEN);

var Interval = setInterval(function(){
  timer.innerHTML = i;
  i--;

  if (i<=0){

    timer.innerHTML = "Select what applies:";
    startTime = Date.now()
    question.style.display = 'inline';
    awaitReaction()
    clearInterval(Interval);
    }
  }, 
  1750
)

function awaitReaction(){

  reaction.onclick = function(){
    reactionTime = Date.now()-startTime-2000;
    reaction.disabled = true;
    antireaction.disabled = true;
    postReactionTime()
  }

  antireaction.onclick = function(){
    reactionTime = Date.now()-startTime-2000;
    reaction.disabled = true;
    antireaction.disabled = true;
    postReactionTime()
    return
  }
}

function postReactionTime(){
    axios({
      method:'post',
      url:PAGE_URL, 
      data:{'reaction_time':reactionTime},
      headers:{'X-CSRFToken':CSRF_TOKEN,
              "content-type": "application/json"}
    }).then(res => {console.log(res)
                    isClicked = false
                    alert('You reacted in ' + reactionTime + ' milliseconds!')})
    .catch(err => {console.log(err)
                  isClicked = false})
}
