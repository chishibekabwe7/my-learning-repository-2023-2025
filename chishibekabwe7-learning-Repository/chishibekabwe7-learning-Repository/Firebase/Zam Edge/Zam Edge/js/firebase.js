// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCWSeyq5hQwbcv8h_v-BKYcQTQhKSp_AF4",
  authDomain: "zam-edge.firebaseapp.com",
  projectId: "zam-edge",
  storageBucket: "zam-edge.firebasestorage.app",
  messagingSenderId: "737133157933",
  appId: "1:737133157933:web:c09ac714999eecbfdda2a4",
  measurementId: "G-MR0TYZYQSB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);