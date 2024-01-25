/*
URL := https://leetcode.com/problems/design-twitter/
355. Design Twitter

Designing simplified social media timelines -> good problem :-)

*/
class Twitter {

    Map<Integer,Set<Integer>> userFollowers;
    Map<Integer,PriorityQueue<int[]>> userTweets;
    int uuid;
    int feedSizeCap;

    public Twitter() {
        this.userFollowers = new HashMap<Integer,Set<Integer>>();
        this.userTweets = new HashMap<Integer,PriorityQueue<int[]>>();
        uuid = 0;
        this.feedSizeCap = 10;
    }
    
    public void postTweet(int userId, int tweetId) {
        if(!this.userTweets.containsKey(userId)){
            // -1 trick super fast woah
            this.userTweets.put(userId, new PriorityQueue<int[]>((a,b) -> -1*Integer.compare(a[0],b[0])));
        }
        this.userTweets.get(userId).add(new int[]{uuid,tweetId});
        uuid++;
    }
    
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> myLocalNewsFeed = new LinkedList<Integer>();
        // woah Integer class customCompare :-)
        PriorityQueue<int[]> myLocalPq = new PriorityQueue<int[]>((a,b) -> -1*Integer.compare(a[0],b[0]));
        // add friends
        Set<Integer> followers = new HashSet<Integer>();
        followers.add(userId);
        if(this.userFollowers.containsKey(userId)){
            followers.addAll(this.userFollowers.get(userId));
        }
        for(Integer follower: followers){
            if(this.userTweets.containsKey(follower)){
                // deep copy copy constructor saves on coding lines
                PriorityQueue<int[]> pqCopy = new PriorityQueue<int[]>(this.userTweets.get(follower));
                for(int a = 0; a < this.feedSizeCap; a++){
                    if(pqCopy.size() > 0){
                        myLocalPq.add(pqCopy.poll());
                    }
                }
            }
        }
        int a = 0;
        while(a < this.feedSizeCap && myLocalPq.size() > 0){
            myLocalNewsFeed.add((myLocalPq.poll())[1]);
            a++;
        }
        return myLocalNewsFeed;
    }
    
    public void follow(int followerId, int followeeId) {
        if(!this.userFollowers.containsKey(followerId)){
            this.userFollowers.put(followerId, new HashSet<Integer>());
        } 
        this.userFollowers.get(followerId).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if(this.userFollowers.containsKey(followerId)){
            if(this.userFollowers.get(followerId).contains(followeeId)){
                this.userFollowers.get(followerId).remove(followeeId);
            }
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
