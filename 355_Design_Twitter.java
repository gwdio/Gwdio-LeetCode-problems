
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Note:
 * This system is designed to maximize the user experience, meaning that it 
 * trades slower writes with much faster reads. The logic is when a post is
 * made, many of the followers of that post will not be currently scrolling
 * the top of the feed, so the client will not notice if a tweet is pushed to
 * them a little bit later.
 * 
 * Therefore, this system holds on to a user's feed on the user side, so when
 * a request for the feed is made, it already exists and the process is effectively
 * instant. The tradeoff is that making a post takes longer, and based on the
 * design, this ends up being slower assuming chained requests like this problem
 * describes.
 * 
 * However, if you assume a testcase that discounts up to 10 ms of processing time,
 * like seen below
 * 
 * <pre>
 *  Program: Post 
 *  Timer: Wait up to 10ms, then ClockStarts
 *  Program: GetFeed
 * </pre>
 * 
 * Then the below implementation will be much faster.
 * 
 * This is more of a real use case, substituting 10 ms for the acceptable time of 
 * delay between a post and receiving a response in this toy model.
 * 
 * The current implementation still has all users keep a very long chain of messages,
 * meaning that receiving a post is as fast as can be O(numfollowers), and getting
 * a feed is near-instant O(1), but subscribing and unsubscribing both take 
 * O(yourPosts + theirPosts) time, which is quite bad, but acceptable considering
 * subscribing is much rarer than all the other operations.
 */
@SuppressWarnings("unused")
class Twitter {
    private final Map<Integer, User> users;
    private int time;

    public Twitter() {
        this.users = new HashMap<>();
        this.time = 0;
    }
    
    public void postTweet(int userId, int tweetId) {
        User usr = getOrCreate(userId);
        usr.post(tweetId, time++);
    }
    
    public List<Integer> getNewsFeed(int userId) {
        User usr = getOrCreate(userId);
        List<Tweet> feed = usr.feed();
        return feed.stream().map(twt -> twt.tweetId()).collect(Collectors.toList());
    }
    
    public void follow(int followerId, int followeeId) {
        User follower = getOrCreate(followerId);
        User followee = getOrCreate(followeeId);
        followee.subscribe(follower);
    }
    
    public void unfollow(int followerId, int followeeId) {
        User follower = getOrCreate(followerId);
        User followee = getOrCreate(followeeId);
        follower.unsubscribe(followee);
    }

    private User getOrCreate(int uid) {
        if (users.get(uid) == null) {
            users.put(uid, new User(uid));
        }
        return users.get(uid);
    }
}

class User {
    private final int uid;
    private final List<User> followers;
    private final Deque<Tweet> feed;

    public User(int uid) {
        this.uid = uid;
        this.followers = new ArrayList<>();
        this.feed = new ArrayDeque<>();
    }

    void subscribe(User follower) {
        if (this.followers.contains(follower)) {
            return;
        }
        this.followers.add(follower);

        // All my (followee's) own past tweets, newest-first
        Deque<Tweet> myPast = this.feed.stream()
            .filter(t -> t.usr() == this)
            .collect(Collectors.toCollection(ArrayDeque::new));
        Deque<Tweet> theirFeed = new ArrayDeque<>(follower.feed);
        List<Tweet> merged = new ArrayList<>();

        while (!myPast.isEmpty() && !theirFeed.isEmpty()) {
            if (myPast.peekFirst().time() > theirFeed.peekFirst().time()) {
                merged.add(myPast.removeFirst());
            } else {
                merged.add(theirFeed.removeFirst());
            }
        }
        merged.addAll(myPast);
        merged.addAll(theirFeed);

        follower.feed.clear();
        follower.feed.addAll(merged);
    }

    void unsubscribe(User unsub) {
        this.followers.remove(unsub);
        feed.removeIf(twt -> twt.usr() == unsub);
    }

    void post(int tweetId, int time) {
        Tweet twt = new Tweet(this, tweetId, time);
        for (User follower : followers) {
            follower.receive(twt);
        }
        this.receive(twt);
    }

    void receive(Tweet twt) {
        feed.addFirst(twt);
    }

    List<Tweet> feed() {
        return new ArrayList<>(this.feed).subList(0, Math.min(10, this.feed.size()));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o instanceof User u) {
            return this.uid == u.uid;
        }
        return false;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(uid);
    }
}

class Tweet {
    private final User usr;
    private final int tweetId;
    private final int time;

    public Tweet(User usr, int tweetId, int time) {
        this.usr = usr;
        this.tweetId = tweetId;
        this.time = time;
    }

    public User usr() {
        return usr;
    }

    public int tweetId() {
        return tweetId;
    }

    public int time() {
        return time;
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