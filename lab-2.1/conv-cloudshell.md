# E2-Standard-4 running in Cloud Shell

Simple conversation with 2 turns

| User              | Agent      |
| ----------------- | ---------- |
| Hi there          | <response> |
| Tell me about GKE | <response> |

````json
INFO:     127.0.0.1:36186 - "POST /sessions HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776/events",
  "status_code": 200,
  "duration_seconds": 0.312
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776",
  "status_code": 200,
  "duration_seconds": 0.369
}
INFO:     127.0.0.1:54132 - "POST /chat HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776",
  "status_code": 200,
  "duration_seconds": 0.304
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776/events",
  "status_code": 200,
  "duration_seconds": 0.308
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.312
}
INFO:google_adk.google.adk.models.google_llm:Sending out request, model: gemini-2.5-flas...d: GoogleLLMVariant.VERTEX_AI, stream: True
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/global/publishers/google/models/gemini-2.5-flash-lite:streamGenerateContent?alt=sse",
  "status_code": 200,
  "duration_seconds": 0.54
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.309
}
INFO:sessions_server:runner.run_async enumeration loop completed in 2.3227 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776",
  "status_code": 200,
  "duration_seconds": 5.329
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776/events",
  "status_code": 200,
  "duration_seconds": 10.3
}
INFO:sessions_server:Updated session get completed in 10.4886 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776/events",
  "status_code": 200,
  "duration_seconds": 0.327
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776",
  "status_code": 200,
  "duration_seconds": 0.331
}
INFO:     127.0.0.1:45728 - "POST /chat HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776/events",
  "status_code": 200,
  "duration_seconds": 0.351
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776",
  "status_code": 200,
  "duration_seconds": 5.347
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.296
}
INFO:google_adk.google.adk.models.google_llm:Sending out request, model: gemini-2.5-flas...d: GoogleLLMVariant.VERTEX_AI, stream: True
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/global/publishers/google/models/gemini-2.5-flash-lite:streamGenerateContent?alt=sse",
  "status_code": 200,
  "duration_seconds": 0.408
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.317
}
INFO:sessions_server:runner.run_async enumeration loop completed in 7.4540 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776/events",
  "status_code": 200,
  "duration_seconds": 0.308
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/8697928349202251776",
  "status_code": 200,
  "duration_seconds": 5.287
}
INFO:sessions_server:Updated session get completed in 5.4740 seconds

````