const body = document.querySelector("body");
const modal = document.querySelector(".modal");
const modalButton = document.querySelector(".modal-button");
const closeButton = document.querySelector(".close-button");
const scrollDown = document.querySelector(".scroll-down");
const openRegisterModalButton = document.querySelector('.open-signup')
const closeSignupButton = document.querySelector('.signup-close-button')
const registerModal = document.querySelector('.signup-modal')
let isOpened = false;

const openModal = (e) => {
  e.preventDefault();
  modal.classList.add("is-open");
  body.style.overflow = "hidden";
};

const openSignUpModal = (e) => {
  e.preventDefault();
  registerModal.classList.add("is-open");
  body.style.overflow = "hidden";
}

const closeModal = () => {
  modal.classList.remove("is-open");
  body.style.overflow = "initial";
};

const closeSignupModal = () => {
  registerModal.classList.remove("is-open");
  body.style.overflow = "initial";
};


modalButton.addEventListener("click", openModal);
openRegisterModalButton.addEventListener("click", openSignUpModal);
closeButton.addEventListener("click", closeModal);
closeSignupButton.addEventListener("click", closeSignupModal);
// modal.addEventListener("click", closeModal)


document.onkeydown = evt => {
  evt = evt || window.event;
  evt.keyCode === 27 ? closeModal() : false;
};