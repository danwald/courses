import { useState } from "react";

function Component() {
  const [text, setText] = useState("");
  const [email, setEmail] = useState("");

  return (
    <div>
      <h2>Events example</h2>
      <form className="form">
        <input
          type="text"
          className="form-input mb-1"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <input
          type="email"
          className="form-input mb-1"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit" className="btn btn-block">
          submit
        </button>
      </form>
    </div>
  );
}

export default Component;
