const rxjs = require('rxjs')
let obs = new rxjs.Observable(observer=>{
  observer.next("Someone");
  observer.next("called");
  observer.next("me");
});
obs.subscribe(element=>{
  console.log(element)
})





let p = new Promise((resolve, reject)=>{
  setTimeout(()=>{
    resolve("Timeout with success........."); //This will be resolved
    resolve("will not be resolved");
    reject("will not be rejected, nothing will work because promises expect only one statement..... resolve or reject");
  }, 1000);
});

p.then(success=>{
  console.log(success);
}, error=>{
  console.log(error);
})  
