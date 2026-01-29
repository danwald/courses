import React, { PropsWithChildren } from 'react';
type ComponentProps = {
  name: string;
  id: number;
  children?: React.ReactNode;
}

type ComponentPropsWithChildren = PropsWithChildren<ComponentProps>;

function Component({ name, id, children }: ComponentPropsWithChildren) {
  return (
    <div>
      <h2>Name: {name}</h2>
      <h2>Id {id}</h2>
      {children}
    </div>
  );
}
export default Component;
