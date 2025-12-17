import { StatsigClient } from '@statsig/js-client';


const client = new StatsigClient(
  process.env.STATSIG_SECRET,
  { userID: 'a-user' },
  {
    environment: { tier: 'development' },
  },
);

client.initializeSync();

let message: string = 'Hello, World!';
console.log(message);
