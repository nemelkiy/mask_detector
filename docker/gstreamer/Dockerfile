FROM restreamio/gstreamer

ENV DEBUG=false
ENV OPTIMIZATIONS=true

RUN ["/compile"]

FROM restreamio/gstreamer:prod-base

COPY --from=0 /compiled-binaries /