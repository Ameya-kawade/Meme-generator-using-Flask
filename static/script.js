document.addEventListener('DOMContentLoaded',() =>{
    let btn = document.getElementById('button');
    let meme_title = document.getElementById('title');
    let meme_img = document.getElementById('img');

    btn.addEventListener('click',()=>{
        let xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_meme',true);

        xhr.onload = ()=>{
            if(xhr.status >= 200 && xhr.status <= 400){
                let response_data = JSON.parse(xhr.responseText);
                meme_img.src = response_data.img; 
                meme_img.onload = ()=>{
                    meme_title.textContent = response_data.title; 
                }
               
                
            }
            else{
                console.log('Error: ' + xhr.statusText);
            }
        };

        xhr.onerror = ()=>{
            console.log('Error');
        }

        xhr.send();
    });
});