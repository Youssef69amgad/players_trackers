# players_trackers
Soccer Player Tracker is a computer vision project designed to track players in football (soccer) videos in real-time. The system detects players and keeps track of their movements across frames, assigning consistent IDs to each player.

Features
Real-time tracking of soccer players in videos.
Uses YOLOv10 for player detection.
Implements ByteTrack tracker for consistent ID assignment and smooth tracking.
Displays annotated video with bounding boxes and player IDs.
Can handle occlusions and fast movements on the field.
Dataset
The project works on football match videos.
Players are detected using a pre-trained YOLO model.
No additional labeling is required for tracking, but detection quality affects tracking performance.
Tracking
The model detects players in each video frame.
ByteTrack maintains the identity of each player over time.
Counts and IDs players as they move across the pitch.
Allows for statistics or analytics on player movement if needed.
Performance
Works efficiently on modern GPUs.
Robust to occlusions and multiple players in close proximity.
Can be extended to include ball tracking, team analysis, or tactical insights.
Notes
Video resolution affects detection and tracking accuracy.
Tracking performance depends on the confidence threshold and IOU settings.
The system can be adapted for other sports or multi-object tracking scenarios.
