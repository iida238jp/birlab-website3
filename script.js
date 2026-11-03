/* Navigation is functional without JavaScript; Escape closes the mobile menu. */
document.addEventListener('keydown',function(event){
  if(event.key==='Escape'){
    const menu=document.querySelector('.mobile-navigation');
    if(menu&&menu.open){menu.open=false;menu.querySelector('summary').focus();}
  }
});
