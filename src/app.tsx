import {
    ControlBar,
    GridLayout,
    ParticipantTile,
    RoomAudioRenderer,
    useTracks,
    RoomContext,
  } from '@livekit/components-react';
  import { Room, Track } from 'livekit-client';
  import '@livekit/components-styles';
  import { useState } from 'react';
  
  const serverUrl = 'wss://recuritflow-6oznsb8q.livekit.cloud';
  const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDk0MDg3NDAsImlzcyI6IkFQSWV3SFg4U3hxMlRqZyIsIm5iZiI6MTc0OTQwMTU0MCwic3ViIjoicXVpY2tzdGFydCB1c2VyIGdkcmw5dyIsInZpZGVvIjp7ImNhblB1Ymxpc2giOnRydWUsImNhblB1Ymxpc2hEYXRhIjp0cnVlLCJjYW5TdWJzY3JpYmUiOnRydWUsInJvb20iOiJxdWlja3N0YXJ0IHJvb20iLCJyb29tSm9pbiI6dHJ1ZX19.zkxpISW2M5wYFlFywLe4BXqXaskstHRGAIZPas6RCkI';
  
  export default function App() {
    const [room] = useState(() => new Room({
      // Optimize video quality for each participant's screen
      adaptiveStream: true,
      // Enable automatic audio/video quality optimization
      dynacast: true,
    }));
  
    // Connect to room
    useEffect(() => {
      let mounted = true;
      
      const connect = async () => {
        if (mounted) {
          await room.connect(serverUrl, token);
        }
      };
      connect();
  
      return () => {
        mounted = false;
        room.disconnect();
      };
    }, [room]);
  
    return (
      <RoomContext.Provider value={room}>
        <div data-lk-theme="default" style={{ height: '100vh' }}>
          {/* Your custom component with basic video conferencing functionality. */}
          <MyVideoConference />
          {/* The RoomAudioRenderer takes care of room-wide audio for you. */}
          <RoomAudioRenderer />
          {/* Controls for the user to start/stop audio, video, and screen share tracks */}
          <ControlBar />
        </div>
      </RoomContext.Provider>
    );
  }
  
  function MyVideoConference() {
    // `useTracks` returns all camera and screen share tracks. If a user
    // joins without a published camera track, a placeholder track is returned.
    const tracks = useTracks(
      [
        { source: Track.Source.Camera, withPlaceholder: true },
        { source: Track.Source.ScreenShare, withPlaceholder: false },
      ],
      { onlySubscribed: false },
    );
    return (
      <GridLayout tracks={tracks} style={{ height: 'calc(100vh - var(--lk-control-bar-height))' }}>
        {/* The GridLayout accepts zero or one child. The child is used
        as a template to render all passed in tracks. */}
        <ParticipantTile />
      </GridLayout>
    );
  }