<h2>1554. Strings Differ by One Character</h2><h3>Medium</h3><hr><div><p>Given a list&nbsp;of strings <code>dict</code> where all the strings are of the same length.</p>

<p>Return <code>True</code> if there are 2 strings that only differ by 1 character in the same index, otherwise&nbsp;return <code>False</code>.</p>

<p><strong>Follow up:&nbsp;</strong>Could you solve this problem in O(n*m) where n is the length of <code>dict</code> and m is the length of each string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> dict = ["abcd","acbd", "aacd"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Strings "a<strong>b</strong>cd" and "a<strong>a</strong>cd" differ only by one character in the index 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> dict = ["ab","cd","yz"]
<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> dict = ["abcd","cccc","abyd","abab"]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>Number of characters in <code>dict &lt;= 10^5</code></li>
	<li><code>dict[i].length == dict[j].length</code></li>
	<li><code>dict[i]</code> should be unique.</li>
	<li><code>dict[i]</code> contains only lowercase English letters.</li>
</ul>
</div>