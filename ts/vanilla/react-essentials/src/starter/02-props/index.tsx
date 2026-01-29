import { PropsWithChildren } from 'react';
type ComponentProps = PropsWithChildren<{
  name: string;
  id: number;
}>

function Component({ name, id, children }: ComponentProps) {
  return (
    <div>
      <h2>Name: {name}</h2>
      <h2>Id {id}</h2>
      {children}
    </div>
  );
}
export default Component;
