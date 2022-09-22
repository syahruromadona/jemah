const selectedText = document.getElementById('selectedText');

window.addEventListener('mouseup', () => {
    const selected = window.getSelection().toString()
    
    if (selected !== ''){
      console.log(selected)
      selectedText.innerText = selected;
    }
    
})

