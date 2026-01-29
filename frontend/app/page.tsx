"use client";

import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent } from "@/components/ui/card";

const API = "http://127.0.0.1:8000";

export default function Home() {
  const [text, setText] = useState("");
  const [entries, setEntries] = useState<any[]>([]);
  const [reflection, setReflection] = useState<any>(null);

  async function welcome() {
    const res = await fetch(`${API}/`);

    return await res.json();



  }










  async function loadEntries() {
    const res = await fetch(`${API}/entries/latest`);
    const data = await res.json();
    setEntries(data.entries);
  }

  async function loadReflection() {
    const res = await fetch(`${API}/reflect`);
    const data = await res.json();
    setReflection(data);
  }

  async function saveEntry() {
    if (!text.trim()) return;

    await fetch(`${API}/entry`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    setText("");
    loadEntries();
    loadReflection();
  }

  useEffect(() => {
    loadEntries();
    loadReflection();
  }, []);

  return (
    <main className="min-h-screen bg-background p-8">
      <div className="max-w-3xl mx-auto space-y-6">

        <h1 className="text-3xl font-bold">MindLedger</h1>

        {/* Write Entry */}
        <Card>
          <CardContent className="space-y-3 pt-6">
            <Textarea
              placeholder="Write how you feel..."
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
            <Button onClick={saveEntry}>Save Entry</Button>
          </CardContent>
        </Card>

        {/* Reflection */}
        <Card>
          <CardContent className="pt-6">
            <h2 className="font-semibold mb-2">Reflection</h2>

            {!reflection ? (
              <p>Loading...</p>
            ) : (
              <div className="text-sm space-y-2">
                <p>
                  Most common emotion:{" "}
                  <b>
                    {reflection.most_common
                      ? `${reflection.most_common[0]} (${reflection.most_common[1]})`
                      : "N/A"}
                  </b>
                </p>

                <pre className="bg-muted p-3 rounded text-xs overflow-auto">
                  {JSON.stringify(reflection.weekly, null, 2)}
                </pre>

                <p>{reflection.comparison}</p>
              </div>
            )}
          </CardContent>
        </Card>

        {/* Entries */}
        <div className="space-y-3">
          {entries.map((e, i) => (
            <Card key={i}>
              <CardContent className="pt-6">
                <p>{e[0]}</p>
                <p className="text-xs text-muted-foreground mt-1">
                  {e[1]} — {e[2]}
                </p>
              </CardContent>
            </Card>
          ))}
        </div>

      </div>
    </main>
  );
}

