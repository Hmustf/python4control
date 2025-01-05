// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getDatabase, ref, runTransaction } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-database.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyA7yzeFkg5iRGlFcd2Jc9SA0MeLltGQ6_o",
    authDomain: "python4control-docs.firebaseapp.com",
    databaseURL: "https://python4control-docs-default-rtdb.firebaseio.com",
    projectId: "python4control-docs",
    storageBucket: "python4control-docs.firebasestorage.app",
    messagingSenderId: "204322242506",
    appId: "1:204322242506:web:fbbfc490403f9840921933",
    measurementId: "G-HLVL8070EK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

export { database, ref, runTransaction }; 