import { useState } from "react";

const navlinks: Link[] = [
  {
    id: 1,
    url: 'some url',
    text: 'some text',
  },
  {
    id: 2,
    url: 'some url',
    text: 'some text',
  },
  {
    id: 3,
    url: 'some url',
    text: 'some text',
  },
]
type Link = {
  id: number;
  url: string;
  text: string;
}
function Component() {
  const [text, setText] = useState<string>("shakeAndBake");
  const [links, setLinks] = useState<Link[]>(navlinks);
  return (
    <div>
      <h2 className="mb-1">React & Typescript</h2>
      <button className="btn btn-center"
        onClick={() => {
          setText("foobar");
          setLinks([...navlinks, { id: 4, text: 'some text', url: 'some url' }]);
        }} >Click Me</button>
    </div >
  );
}
export default Component;
