from django.http import HttpResponse

# Create your views here.
from django.template.response import SimpleTemplateResponse

from core.models import Vision, Volume


def index(request):
    return HttpResponse("Hello world - this is the initial index view.")

def plain_text_vision(request, pk):
    vision = Vision.objects.get(pk=pk)
    return SimpleTemplateResponse(template="plain_text_vision.txt", context={"vision": vision},
                                  content_type="text/plain")

def _title_for_output(volume_list):
    if len(volume_list) == 1:
        return volume_list[0].volume_title

def _join_names_naturally(name_list):
    assert len(name_list) > 0
    if len(name_list) == 1:
        return name_list[0]
    if len(name_list) == 2:
        return "{l[0]} and {l[1]}".format(l=name_list)
    else:
        return "{joined}, {second_last}, and {last}".format(joined=", ".join([n.name for n in name_list[:-2]]),
                                                            second_last=name_list[-2],
                                                            last=name_list[-1])

def _contributor_credits_for_output(volume_list):
    credits = []
    for writer_type in ('notes', 'accounts', 'commentary'):
        writers = volume_list[0].writers_for_volume(writer_type).union(
            *[v.writers_for_volume(writer_type) for v in volume_list[1:]])
        if len(writers) > 0:
            # Only include it if we have anything in that list. This is only an issue for commentary,
            # as notes and accounts will always be credited.
            credits.append("{output} by {writers}.".format(
                output=writer_type.title(),
                writers=_join_names_naturally(list(writers)))
            )
    return "\n".join(credits)

def _front_page_credits_for_output(volume_list):
    # TODO: I'm thinking of doing this differently, but to start with, do it using v.writers_for_volume("notes").
    writers = volume_list[0].writers_for_volume("notes").union(
        *[v.writers_for_volume("notes") for v in volume_list[1:]])
    return [writer.name for writer in writers]

def _volume_number_dates_for_output(volume_list):
    assert len(volume_list) > 0
    if len(volume_list) == 1:
        return "Volume {v.number}: {v.volume_date}".format(v=volume_list[0])
    else:
        sorted_volumes = sorted(volume_list, key=lambda volume: volume.number)
        return "Volume {first.number}-{last.number}: {first.volume_date}-{last.volume_date}".format(
            first=sorted_volumes[0], last=sorted_volumes[-1]
        )

def plain_text_single_volume(request, volume_number):
    volume = Volume.objects.get(number=volume_number)
    # TODO: When we've got this working as a single-event template, extend it to cover multiple events.
    # TODO: Properly implement volume credits rather than just using the notes credits.
    # TODO: Add the "N visionaries at this summit" paragraph, ideally with source attributions but optionally not.
    return SimpleTemplateResponse(template="plain_text_volume.txt",
                                  context={
                                      "volume": volume,
                                      "contributor_credits": _contributor_credits_for_output([volume]),
                                      "front_page_credits": _front_page_credits_for_output([volume]),
                                      "number_and_dates": _volume_number_dates_for_output([volume]),
                                  },
                                  content_type="text/plain")
