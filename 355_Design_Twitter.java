
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

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