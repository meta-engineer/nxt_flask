# NXT

## App Design Bird's-Eye

1. One Time Splash page
	- just text/graphics?
	- *navigate to 2.Login*
2. Login
	- integrate with Google login?
	- cookies/sessions?
	- *navigate to 3.Home*
3. Home
	- navigation
	- user info?
	- *navigate to 4.Profile, 5.Suppliments, 6.Catalog, 7.Tracker/Stats, 8.Social, 9.Routine*
4. Profile
	- remote database server for user data
	- "Player Card": query user table
	- Stats
		- images: profile picture
		- static size stats: individual 1RM, lift deltas, streaks, max inspirations
		- dynamic size stats: awards, weight tracking, program progress
	- Journal entries
	- integrate social media?
	- *navigate to 3.Home*
5. Suppliments
	- storefront: set/user query suppliments table
	- integration to payment service? paypal?
	- *navigate to 3.Home*
6. Exercises
	- catalog: set/user query exercise table
	- subtables: program, muscle group, goal
	- query user data for permissions
	- GIF/VIDEO storage (multiple videos? short/long versions?)
	- *navigate to 3.Home*
7. Tracker/Stats
	- what is this, statistics about ants?
	- some sort of accessor to logged-in user table
	- *navigate to 3.Home*
8. Social
	- friends/leaderboards
	- search user table for names? view "player card" or some other static size query?
	- at best just queries to user tables and displaying top results
	- at worst message posting/realtime chat
	- database table for timed challenges? storage for top scores?
	- *navigate to 3.Home*
9. Routines
	- table with list of {sets, reps, exercise}
	- complicated details? rest between sets? supersets?
	- metadata: written information/description
	- gif/video per exercise (query exercise table)
	- store user progress for particular routine in user table. hash map to routines table?
	- *navigate to 3.Home*
