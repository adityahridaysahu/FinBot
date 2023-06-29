// import React, { useState } from "react";
// import "./App.css";
// import Navbar from "./components/Navbar/Navbar";
// import Card from "./components/Card/Card";
// import Footer from "./components/Footer/Footer";
// import Data from "./data/data";
// import Chatbot from "react-chatbot-kit";
// import "react-chatbot-kit/build/main.css";
// // import ChatbotInterface from "./components/ChatBot";

// const App: React.FC = () => {
//   const cards = Data.map(item => {
//     return (
//       <Card
//         key={item.id}
//         {...item}
//       />
//     )
//   })

//   const [showChatbot, setShowChatbot] = useState(false);

//   const toggleChatbot = () => {
//     setShowChatbot(!showChatbot);
//     if (showChatbot) {
//       window.location.reload();
//     }
//   };

//   return (
//     <div className="App">
//       <Navbar />
//       <main>
//         {cards}
//         {/* <div className="card">
//           {showChatbot ? <ChatbotInterface /> : null}
//         </div> */}
//         {showChatbot ? (
//         <p></p>
//       ) : (
//         <div className="chatbot-toggle">
//           <button
//             data-testid="new-chat-button"
//             className={showChatbot ? "" : "btn"}
//             onClick={toggleChatbot}
//           >
//             {showChatbot ? "" : "New Chat"}
//           </button>
//         </div>
//       )}
//       </main>
//       <Footer />
//     </div>
//   );
// }

// export default App;
