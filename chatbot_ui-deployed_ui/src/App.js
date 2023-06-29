import React, { useState } from "react";
import ChatbotInterface from "./chatbot";
import "react-chatbot-kit/build/main.css";
import "./new.css";
import logo from "./logo.png";
import Navbar from "./components/Navbar/Navbar";
import Card from "./components/Card/Card";
import Footer from "./components/Footer/Footer";
import Data from "./data/data";

const App = () => {
  const cards = Data.map((item) => {
    return <Card key={item.id} {...item} />;
  });

  const [showChatbot, setShowChatbot] = useState(false);

  const toggleChatbot = () => {
    setShowChatbot(!showChatbot);
    if (showChatbot) {
      window.location.reload(false);
    }
  };

  return (
    <div className="app">
      <Navbar />
      {/* <div className="header">{showChatbot ? <ChatbotInterface /> : null}</div> */}
      <main>
        <div style={{ marginTop: "20px" }}>
          {cards}
        {/* </div> */}
        {showChatbot ? <ChatbotInterface /> : null}
        {showChatbot ? (
          <p></p>
        ) : (
          <div className="chatbot-toggle">
            <button
              data-testid="new-chat-button"
              className={showChatbot ? "" : "btn"}
              onClick={toggleChatbot}
            >
              {showChatbot ? "" : "New Chat"}
            </button>
          </div>
        )}
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default App;
