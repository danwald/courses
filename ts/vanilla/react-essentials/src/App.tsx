import Component from './starter/02-props/'


function App() {
  return (
    <main>
      <Component name='Danny' id={123}>
        <h3> befriends</h3>
      </Component>
      <Component name='Thanda' id={345} />
    </main>
  );
}
export default App;
