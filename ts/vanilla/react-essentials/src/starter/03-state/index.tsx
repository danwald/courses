import { useState } from "react";


function Component() {
  const [text, setText] = useState<string>("shakeAndBake");
  return (
    <div>
      <h2 className="mb-1">React & Typescript</h2>
      <button className="btn btn-center" onClick={() => { setText("foobar") }}>Click Me</button>
    </div >
  );
}
export default Component;
