type ComponentProps = {
  name: string;
  id: number;

}

function Component({ name, id }: ComponentProps) {
  return (
    <div>
      <h2>Name: {name}</h2>
      <h2>Id {id}</h2>
    </div>
  );
}
export default Component;
